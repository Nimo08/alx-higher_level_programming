#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer
 * Return: 1 if it's a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int cnt = 0;

	ptr = *head;
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	while (ptr != NULL)
	{
		ptr = ptr->next;
		cnt++;
	}
	if (cnt % 2 == 0)
	{
		return (1);
	}
	return (0);
}
