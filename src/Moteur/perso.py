import sys




def main():
    avatar = Avatar()
    for i in range(5):
        avatar.deplacer()
        print("positionX = " + str(avatar.positionX) + ", positionY = " + str(avatar.positionY))

    end
    #for i in range(5):
    #    avatar.deplacer()
    #    print("positionX = " + avatar.positionX + "positionY = " + avatar.positionY)
    # end

if __name__ == '__main__':
    main()

