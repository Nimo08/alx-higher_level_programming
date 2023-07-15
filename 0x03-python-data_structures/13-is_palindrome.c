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
	listint_t *temp;

	ptr = *head;
	temp = NULL;
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		if (ptr == temp)
		{
			return (0);
		}
	}
	return (1);
}
