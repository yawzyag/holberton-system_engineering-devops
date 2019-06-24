#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: lenght of string
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - child pd
 *
 * Return: 0 always
 */

int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
			sleep(1);
		else
			return (0);
		printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();
	return (0);
}
