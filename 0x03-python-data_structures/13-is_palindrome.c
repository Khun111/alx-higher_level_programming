#include "lists.h"
listint_t *rev_half(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * rev_half - reverses list
 * @head: pointer to list head
 * Return: pointer to reversed list head
 */
listint_t *rev_half(listint_t **head)
{
    listint_t *current = *head, *prev = NULL, *next;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return (*head);
}
/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to list head
 * Return: 0/1
 */
int is_palindrome(listint_t **head)
{
    listint_t *cursor, *reversed, *half
    size_t size = 0, i = 0;

    if (*head == NULL || (*head)->next == NULL)
        return (1);
    cursor = *head;
    while (cursor)
    {
        size++;
        cursor = cursor->next;
    }

    cursor = *head;
    for (; i < (size / 2) - 1, i++)
        cursor = cursor->next;
    if ((size & 2) == 0 && cursor->n != cursor->next->n)
        return (0);
    cursor = cursor->next->next;
    reversed = rev_half(&tmp);
    half = reversed;

    cursor = *head;
    while (reversed)
    {
        if (cursor->n != reversed->n)
            return (0);
        cursor = cursor->next;
        reversed = reversed->next;
    }
    rev_half(&mid);
    return (1);
}