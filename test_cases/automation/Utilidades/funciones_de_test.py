from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
import Utilidades.random_email as RE

# funcion para llenar un campo de texto pasando el input, el driver y el elemento a llenar


def input_field(input, driver, element):
    try:
        # esperamos a que el elemento con el nombre de clase "home-textinput" este presente en la pagina (max 5 segs)
        field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(element)
        )
        field.send_keys(input)
    # si no se carga la pagina en 10 segundos, imprimo un mensaje de error
    except:
        print("No encontro el elemento", element)


def input_fields(inputs, driver, elements):
    try:
        # esperamos a que el elemento con el nombre de clase "home-textinput" este presente en la pagina (max 5 segs)
        fields = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located(elements)
        )
        i = 0
        for field in fields:
            field.send_keys(inputs[i])
            i += 1
    # si no se carga la pagina en 10 segundos, imprimo un mensaje de error
    except:
        print("No encontro el elemento", elements)


def input_field_by_one(input, driver, element):
    try:
        # esperamos a que el elemento con el nombre de clase "home-textinput" este presente en la pagina (max 5 segs)
        field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(element)
        )
        for char in input:
            field.send_keys(char)
            time.sleep(0.5)
    # si no se carga la pagina en 10 segundos, imprimo un mensaje de error
    except:
        print("No encontro el elemento", element)


# funcion para hacer click en un boton pasando el driver y el elemento a clickear


def click_button(driver, element):
    try:
        # esperamos a que el elemento este presente en la pagina (max 5 segs)
        button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(element))

        button.click()
    # si no se carga la pagina en 10 segundos, imprimo un mensaje de error
    except:
        print("No encontro el elemento", element)


def clear_field(driver, element):
    try:
        # esperamos a que el elemento este presente en la pagina (max 5 segs)
        field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(element))

        field.clear()
    # si no se carga la pagina en 10 segundos, imprimo un mensaje de error
    except:
        print("No encontro el elemento", element)
