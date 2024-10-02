# socket_presentation

The training is going through the different syscalls available from the kernel.  

We start with the server script, executing up to the listen syscall.  
Then we move on to the client side and executing it completely (but do not exit the script after "send").


1- the `socket` system call

The socket syscall is to tell the kernel what type of transport you want to be using.  

The first part is the technology for the socket (Address Family) ; 
- IP (IPV4 -> AF_INET, IPV6 -> AF_INET6)
- Bluetooth (AF_BLUETOOTH)
- UNIX file (AF_UNIX)
- etc.

The second part is the type of socket it will be over the technology;
- SOCK_STREAM (TCP)
- SOCK_DGRAM (message-based) (UDP)

The rest of the parameters are optional as they can be infered by the kernel (proto=0), but they represent the specific protocol to use (e.g. TCP and SCTP are both stream protocol, but to use SCTP, you would specify 132 in the proto parameter to tell the kernel you want SCTP explicitly).

This is one of the most important syscall as it basically setup the file we're going to use.  There is a lot of knowledge that needs to be known to make it correctly (we'll get to how to prepare them accordingly later).

2- The `bind` system call

This is the call that will reserve the resource in the kernel for your usage.  This is informing the kernel that you plan on using a resource (the address) and wish to become it's owner.  While it's the kernel that will either tell you no (the address is already in use) or yes (no exception or return code of 0), you can decide to share this address as well (but then you need to set up the socket options first).  

Recall that most protocol have a source and destination port, this will become important later.

TO BE CONTINUED
