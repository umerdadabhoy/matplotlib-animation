import matplotlib.pyplot as plt
#declaring default value of variables
x = None
y = None

#declaring figure with size 10,10
fig =  plt.figure()

#file name history
filenames=[]

for i in range(0,10):
    #setting figure axis limits , so every iteration have same axis
    plt.xlim(0,10)
    plt.ylim(0,20)
    #drawing point
    x = i
    y = i*2
    z = plt.plot(x,y,'o')
    
    
    #saving each 
    filename = f'{i}.png'
    #adding names to list
    filenames.append(filename)
    plt.savefig(filename)
    
    
    #unhash when you want just display of animation , without saving files 
    #plt.pause(0.5)
    #use plt.draw instead of plt.show to display all drawing in same figure
    #plt.draw()

    plt.close()
    #z.pop very important , other wise blank fig with z.remove
    z = z.pop(0)
    z.remove()
    
import imageio
import os

#creating gif
with imageio.get_writer("graph_animie.gif" , mode = 'I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

#deleting all the frames , allowing code utilization for some other image/data
for filename in set(filenames):
    os.remove(filename)

