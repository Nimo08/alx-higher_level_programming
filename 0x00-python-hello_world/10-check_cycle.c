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
	while (slow != fast)
	{
		if (fast == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);

}
