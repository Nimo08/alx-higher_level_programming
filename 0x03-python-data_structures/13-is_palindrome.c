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
	listint_t *first;
	listint_t *last;

	first = *head;
	last = *head;
	if (*head == NULL)
	{
		return (1);
	}
	while (first != NULL && last != NULL && last->next != NULL)
	{
		first = first->next;
		last = last->next->next;
		if (first->n == last->n)
		{
			return (1);
		}
	}
	return (0);
}
