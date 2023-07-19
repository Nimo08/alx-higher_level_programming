#include "Python.h"
/**
 * print_python_bytes - prints python bytes
 * @p: pointer to PyObject
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %lu\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (size >= 10)
			size = 10;
		else
			size += 1;
		printf("  first %lu bytes:", size);
		for (i = 0; i < size; i++)
		{
			printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);
		}
		printf("\n");
	}
	printf("  [ERROR] Invalid Bytes Object\n");
}
/**
 * print_python_list - prints basic info about python lists
 * @p: pointer to PyObject
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *q;
	Py_ssize_t allocated = ((PyListObject *)(p))->allocated;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocated);
	for (i = 0; i < size; i++)
	{
		q = PyList_GET_ITEM(p, i);
		printf("Element %lu: %s\n", i, q->ob_type->tp_name);
		if (PyBytes_CheckExact(q))
		{
			print_python_bytes(p);
		}
	}
}
