import qrcode



upi_id = input("Enter your UPI ID: ").strip()
amt = input("Enter your payment amount: ").strip()

upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amt}&cu=INR&tn=Payment"

# Create and save QR code
qr = qrcode.make(upi_url)
qr.save("upi_qr.png")
qr.show()

