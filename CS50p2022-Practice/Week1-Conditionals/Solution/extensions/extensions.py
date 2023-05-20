# file’s media type
filetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

def main():
    user_file = str(input("File name: ").strip.lower())
    print(filetype_check(user_file))

def filetype_check(user_file):
    if "." in user_file:
        # split() slices the string by the specified delimiter, if the parameter num has the specified value, separates num+1 substrings
        check = user_file.split(".", 1)
        if check[1] not in filetypes:
            return "application/octet-stream"
        else:
            return filetypes[check[1]]
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()