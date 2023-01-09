from PIL import Image

# !!! Put the gif's filename here
gifname = 'test.gif'

with Image.open(gifname) as im:
    # for every frame in gif
    for i in range(im.n_frames):
        # get frame
        im.seek(i)
        # save frame
        im.save(f'{i}.png')
