# Postmortem

![class](https://zahazee.files.wordpress.com/2015/12/img_3378.jpg?w=400&zoom=2)

[postmortem](https://queue.acm.org/detail.cfm?id=2039361)

---



Despite the best efforts of software engineers to produce high-quality software, inevitably some bugs escape even the most rigorous testing process and are first encountered by end users. When this happens, such failures must be understood quickly, the underlying bugs fixed, and deployments patched to avoid another user (or the same one) running into the same problem again. As far back as 1951, the dawn of modern computing, Stanley Gill6 wrote that "some attention has, therefore, been given to the problem of dealing with mistakes after the programme has been tried and found to fail." Gill went on to describe the first use of "the post-mortem technique" in software, whereby the running program was modified to record important system state as it ran so that the programmer could later understand what happened and why the software failed.


## Debugging in the large

To understand the unique value of postmortem debugging, it's worth examining the alternative. Both native and dynamic environments today provide facilities for  _in situ_  debugging, or debugging faulty programs while they're still running. This typically involves attaching a separate debugger program to the faulty program and then directing execution of the faulty program interactively, instruction by instruction or using breakpoints. The user thus stops the program at various points to inspect program state in order to figure out where it goes wrong. Often this process is repeated to test successive theories about the problem.

This technique can be very effective for bugs that are readily reproducible, but it has several drawbacks. First, the act of stopping a program often changes its behavior. Bugs resulting from unexpected interactions between parallel operations (such as race conditions) can be especially challenging to analyze this way because the timing of various events is significantly affected by the debugger itself. More importantly,  _in situ_  debugging is often untenable on production systems: many debuggers rely on an unoptimized debug build that's too slow to run in production; engineers often do not have access to the systems where the program is running (as in the case of most mobile and desktop applications and many enterprise systems); and the requisite debugging tools are often not available on those systems anyway.

Even for cases where engineers can access the buggy softw

## Postmortem debugging in native environments

To understand the potential value of postmortem debugging in dynamic languages, it's also helpful to examine those areas where postmortem analysis techniques are well developed and widely used. The best examples are operating systems and their native execution environments. Historically this software has comprised core infrastructure; failures at this level of the stack are often very costly either because the systems themselves are necessary for business-critical functions (as in the case of operating systems on which business-critical software is running) or because they are relied upon by business-critical systems upstack (as in the case of infrastructure services such as DNS).

---
