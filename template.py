import os
dirs=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "Notebooks",
    "saved_model",
    "src"

]
for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass
file=[
    os.path.join("src","__init__.py"),
    "dvc.yaml",
    ".gitignore",
    "params.yaml"
]
for fl in file:
    with open(fl,"w") as f:
        pass