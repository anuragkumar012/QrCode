import qrcode  # Import the QR code module

# Get UPI ID input from user
upi_id = input("Enter your UPI ID: ")

# Generate UPI Payment URLs for different platforms
phonepe_url = f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc='
google_pay_url = f'googlepay://pay?pa={upi_id}&pn=recipient%20Name&mc='
paytm_url = f'paytm://pay?pa={upi_id}&pn=recipient%20Name&mc='
mobikwik_url = f'mobikwik://pay?pa={upi_id}&pn=recipient%20Name&mc='

# Function to generate and save QR codes
def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box in pixels
        border=4  # Border size
    )
    qr.add_data(data)  # Add UPI URL to QR code
    qr.make(fit=True)

    # Create an image with custom colors
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Generate and save QR codes for all platforms
generate_qr(phonepe_url, "phonepe_qr.png")
generate_qr(google_pay_url, "google_pay_qr.png")
generate_qr(paytm_url, "paytm_qr.png")
generate_qr(mobikwik_url, "mobikwik_qr.png")

# Show QR codes (optional)
import os
if os.name == "nt":  # Windows
    os.system("start phonepe_qr.png")
    os.system("start google_pay_qr.png")
    os.system("start paytm_qr.png")
    os.system("start mobikwik_qr.png")
else:  # Mac/Linux
    os.system("open phonepe_qr.png")
    os.system("open google_pay_qr.png")
    os.system("open paytm_qr.png")
    os.system("open mobikwik_qr.png")
