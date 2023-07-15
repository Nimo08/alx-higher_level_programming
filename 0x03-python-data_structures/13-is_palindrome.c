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
	listint_t *first;
	listint_t *last;

	ptr = *head;
	first = *head;
	last = *head;
	if (first == NULL)
	{
		return (0);
	}
	while (first->next != NULL)
	{
		first = first->next;
		last = last->next;
	}
	while (*head != last)
	{
		while (ptr->next != NULL)
		{
			ptr = ptr->next;
		}
		if (ptr->next != last)
		{
			return (1);
		}
		last = ptr;
		*head = (*head)->next;
	}
	return (0);
}
