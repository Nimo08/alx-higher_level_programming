#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	Py_Object *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		print("Element: %ld: %s\n", i, PY_TYPE(obj)->tp_name);
	}
}
