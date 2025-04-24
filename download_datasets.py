import kagglehub

# Download latest version
dataset_download = 1

if dataset_download == 0 :
    path = kagglehub.dataset_download("atharvasoundankar/impact-of-ai-on-digital-media-2020-2025")
    print("Path to dataset files:", path)


