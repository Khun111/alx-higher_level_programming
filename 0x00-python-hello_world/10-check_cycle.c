#include "lists.h"
/**
 * check_cycle - checks for a cycle in a list
 * @list: list to check
 * Return: 0/1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	if (!list || list->next == NULL)
		return (0);
	slow_p = list->next;
	fast_p = list->next->next;

	while (slow_p && fast_p && fast_p->next)
	{
		if (slow_p == fast_p)
			return (1);
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
	}
	return (0);
}
