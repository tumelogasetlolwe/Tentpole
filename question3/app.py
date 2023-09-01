import os
import time
import sqlite3

def import_new_files(folder_path):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    while True:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):  
                with open(os.path.join(folder_path, filename), 'r') as file:
                    content = file.read()
                    cursor.execute('INSERT INTO files (filename, content) VALUES (?, ?)', (filename, content))
                    conn.commit()
                os.remove(os.path.join(folder_path, filename))  

        time.sleep(60)  # Check for new files every 60 seconds

    conn.close()

if __name__ == '__main__':
    folder_to_monitor = 'folder_to_monitor' 
    import_new_files(folder_to_monitor)
