import mailtrap


api_token="e908d59cade0ab68d91d2e28f5c42062"

def email(to,subject,message):
    mail=mailtrap.Mail( 
        sender=mailtrap.Address(email="Hello@demomailtrap.co",name="FLASK_API"),
        to=[mailtrap.Address(email=to)],
        subject=subject,
        text=message, # message is a parameter/placeholder
        category="mailtrap integration test"
    )
    client=mailtrap.MailtrapClient(token=api_token)
    response=client.send(mail)

    print("-------------this is mailtrap--------------")
    print(response)

# email("loreenwandanje@gmail.com","Testing API","I am testing my API")    

