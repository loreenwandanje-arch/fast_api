import cloudinary
import cloudinary.uploader
from send_email import email

Cloud_Name="tmbushfq"
API_key="618784954273375"
Secret_Key="r_ephDl7PoKL5pmEQCiAgIUt3Dc"

# connecting to cloudinary
cloudinary.config(
    cloud_name= Cloud_Name,
    api_key=API_key,
    api_secret=Secret_Key
)
def upload_pdf(pdf_file):
    try:
        file_path=f"receipts/{pdf_file}.pdf"
        # upload pdf
        upload = cloudinary.uploader.upload(file_path, resource_type="raw")
        receipt_url = upload["secure_url"]
        print("successful cloudinary upload")
        print(receipt_url)
        email("loreenwandanje@gmail.com","Payment Received",f"Thankyou for shopping with us.\n\n" f"Receipt: {receipt_url}")
        return"success"
    except Exception as e:
        print(f"upload failed: {e}")
        return "failed"