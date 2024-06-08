
def get_media_type(file_name):

    media_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }

    extension = file_name.split(".")[-1].lower() if "." in file_name else ""

    media_type = media_types.get(extension, "application/octet-stream")

    return media_type

def main():
    file_name = input("Enter a file name: ").strip()

    media_type = get_media_type(file_name)

    print(media_type)

if __name__ == "__main__":
    main()
