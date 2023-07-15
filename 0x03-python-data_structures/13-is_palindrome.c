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
	listint_t *temp;
	listint_t *ptr;

	temp = NULL;
	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
	{
		return (0);
	}
	if (*head == NULL)
	{
		return (0);
	}
	if (*head == temp)
	{
		return (0);
	}
	while (ptr != NULL)
	{
		ptr = ptr->next;
	}
	return (1);
}
