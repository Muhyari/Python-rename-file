import os
import shutil
import asyncio

async def rename_and_move_files(directory: str, text_want_to_remove: str, move_file_to_dir: str, ekstension: str):
    text_want_to_remove = text_want_to_remove.strip("")
    
    for index, filename in enumerate(os.listdir(directory)):
        if filename.startswith(text_want_to_remove):
            if ekstension in os.path.splitext(filename):
                old_path = os.path.join(directory, filename)
                new_name = filename.replace(text_want_to_remove, "")
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                await asyncio.sleep(1)
                shutil.move(f"{directory}/{new_name}", move_file_to_dir)
        
async def main():
    directory = "folder tempat file yang ingin diubah namanya"
    remove_text = "text yang ingin di hapus"
    music_dir = "tempat file yang akan dipindahkan"
    await rename_and_move_files(directory=directory, text_want_to_remove=remove_text, move_file_to_dir=music_dir, ekstension=".mp3")
    print("file sudah selesai diubah dan dipindahkan")
    
asyncio.run(main())