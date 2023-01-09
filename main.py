from PIL import Image
import os

giffolder = "./gifs"  # gif source folder
outfolder = "./output"  # gif frames output folder

# create a folder
def createfolder(foldername):
    if not os.path.exists(f"./{foldername}"):
        os.makedirs(f"./{foldername}")


# create output folder
createfolder(outfolder)
# for all files in giffolder
for fi in os.listdir(giffolder):
    # if file is of .gif extension
    if fi.split('.')[-1] == 'gif':
        # open image as Pillow(from PIL) Image
        with Image.open(giffolder + "/" + fi) as im:
            print(fi)  # just to update on what the program is working on

            # create destination folder
            createfolder(f'{outfolder}/{fi}')

            # for every frame in gif
            for i in range(im.n_frames):
                # get frame
                im.seek(i)
                # save frame
                im.save(f'{outfolder}/{fi}/{i}.png')
