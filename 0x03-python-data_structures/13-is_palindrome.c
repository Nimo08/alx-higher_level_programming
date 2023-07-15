#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer
 * Return: 0 if it's a palindrome, 1 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int cnt = 0;

	ptr = *head;
	if (head == NULL)
	{
		return (0);
	}
	if (*head == NULL)
	{
		return (1);
	}
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		cnt++;
		if (cnt % 2 == 0)
		{
			return (1);
		}
	}
	return (0);

}
