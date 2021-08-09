objects = main.o usb.o
run: $(objects)
	gcc $(objects) -o run
usb.o:usb.c
	gcc -c usb.c -o usb.o

main.o:main.c
	gcc -c main.c -o main.o
.PHONY: clean
clean:
	rm $(objects) run
