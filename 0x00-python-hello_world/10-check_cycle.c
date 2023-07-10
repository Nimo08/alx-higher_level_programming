#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: struct pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;
	while (slow != NULL && fast != NULL)
	{
		if (fast->next != NULL)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		else
		{
			return (0);
		}
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
