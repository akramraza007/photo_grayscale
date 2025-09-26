import cv2
image_location = input("Put the location of the image: ")
image = cv2.imread(image_location)

if image is None:
    print("Error: Could not load image. Please check the path.")

else:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    op = input("Choose an option:\n1. Show\n2. Save\n")
    if op =="1":
        cv2.imshow("gray",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif op == "2":
        save_name = input("Enter filename to save(e.g., 'output.jpg'):")
        success = cv2.imwrite(save_name,gray)
        if success:
            print(f"Image saved as {save_name}")
        else:
            print("Error: Could not save the image.")
    else:
        print("Wrong input. Please enter 1 for show or 2 for save.")
        
