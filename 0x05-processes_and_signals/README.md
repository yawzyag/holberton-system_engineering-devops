# Processes and signals

![N|process](https://www.linode.com/docs/tools-reference/tools/use-killall-and-kill-to-stop-processes-on-linux/use-killall-and-kill-commands-to-stop-processes-on-linux.png)
reference(https://www.bogotobogo.com/Linux/linux_process_and_signals.php)


The signals and processes control almost every task of the system.

We get the following response at ps -ef:

    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0  2010 ?        00:01:48 init 
    root     21033     1  0 Apr04 ?        00:00:39 crond
    root     24765     1  0 Apr08 ?        00:00:01 /usr/sbin/httpd

# Process State

Each process is allocated a unique number, process identifier (PID). It's an integer between 2 and 32,768. When a process is started, the numbers restart from 2, and the number 1 is typically reserved for the init process as shown in the above example. The process #1 manages other processes.

When we run a program, the code that will be executed is stored in a disk file. In general, a linux process can't write to the memory area. The area is for holding the program code so that the code can be loaded into memory as read-only (so, it can be safely shared).

![N|process](https://www.bogotobogo.com/Linux/images/process/process.png)

The system libraries can also be shared. Therefore, there need be only one copy of printf() in memory, even if there are many programs calling it.

When we run two programs, there are variables unique to each programs, unlike the shared libraries, these are in separate data space of each process, and usually can't be shared. In other words, a process has its own stack space, used for local variables. It also has its own environment variables which are maintained by each process. A process should also has its own program counter, a record of where it has gotten to in its execution (execution thread - more on linux pthread).


## Process Table

The process table describes all the processes that are currently loaded. The ps command shows the processes. By default, it shows only processes that maintain a connection with a terminal, a console, a serial line, or a pseudo terminal. Other processes that can run without communication with a user on a terminal are system processes that Linux manages shared resources. To see all processes, we use -e option and -f to get full information (ps -ef).

## System Processes
Here is the STAT output from ps:

    $ ps -ax
    PID TTY      STAT   TIME COMMAND
    1 ?        Ss     1:48 init [3]
    2 ?        S<     0:03 [migration/0]
    3 ?        SN     0:00 [ksoftirqd/0]
    ....
    2981 ?        S<sl  10:14 auditd
    2983 ?        S<sl   3:43 /sbin/audispd
    ....
    3428 ?        SLs    0:00 ntpd -u ntp:ntp -p /var/run/ntpd.pid -g
    3464 ?        Ss     0:00 rpc.rquotad
    3508 ?        S<     0:00 [nfsd4]
    ....
    3812 tty1     Ss+    0:00 /sbin/mingetty tty1
    3813 tty2     Ss+    0:00 /sbin/mingetty tty2
    3814 tty3     Ss+    0:00 /sbin/mingetty tty3
    3815 tty4     Ss+    0:00 /sbin/mingetty tty4
    .....
    19874 pts/1    R+     0:00 ps -ax
    19875 pts/1    S+     0:00 more
    21033 ?        Ss     0:39 crond
    24765 ?        Ss     0:01 /usr/sbin/httpd
    
The meaning of the code is in the table below:

    STAT Code  Description
    R	 Running or runnable (either executing or about to run).
    D	 Uninterruptible sleep (waiting) - usually waiting for input or output to complete.
    S	 Sleeping. Usually waiting for an event to occur, such as a signal or input to become available.
    T	 Stopped. Usually stopped by shell job control or the process is under the control of a debugger.
    Z	 Defunct or zombie process.
    N	 Low priority task, nice.
    W	 Paging.
    s	 The process is a session leader.
    +	 The process is in the foreground process group.
    l	 The process is multithreaded.
    <	 High priority task.
