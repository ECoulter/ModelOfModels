"""
    monitor.py
        -- service monitor
        -- runs daily
"""
import os, json
from datetime import date
import shutil
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

""" cron data folder """
cron_data_folder = "../data/cron_data/flood_severity"

def sendEmail(status):
    """ send email notification """

    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')
    from_email = config['EMAIL']['from_email']
    to_emails = config['EMAIL']['to_emails']
    sg_key = config['EMAIL']['SENDGRID_API_KEY']

    subject = status['status'] + " : " + status['output']

    if status['diskusage'] == "warning":
        subject += " + warning: low disk"
    
    content_str = json.dumps(status,indent = 4)

    message = Mail(
        from_email=from_email,
        to_emails = to_emails,
        subject = subject,
        html_content = content_str )

    try:
        sg = SendGridAPIClient(sg_key)
        reponse = sg.send(message)
    except Exception as e:
        print(e.message)
    
    return


def checkService():
    """ check service status """

    # get the date
    status = {}
    today = date.today()
    d1 = today.strftime("%Y%m%d")
    status['date'] = d1
    # output: Final_Attributes_20210123.csv
    checkfile = "Final_Attributes_" + d1 + ".csv"
    if os.path.exists(cron_data_folder + os.path.sep + checkfile):
        status["output"] = checkfile + " is produced!"
        status["status"] = "Success"
    else:
        status["output"] = checkfile + " is not produced!"
        status["status"] = "Fail"

    # check diskusage
    # usage(total=250135076864, used=11416207360, free=30952230912)
    diskusage = shutil.disk_usage("/")
    freespace = diskusage.free / (10**9)
    status["freespace"] = str(freespace) + " GB"
    if freespace < 1.0:
        status['diskusage'] = "warning"
    else:
        status['diskusage'] = "Ok"

    sendEmail(status)

def main():
    checkService()

if __name__ == "__main__":
    main()