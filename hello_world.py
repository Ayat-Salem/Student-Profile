{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7447ee05-18a1-46ff-91e0-1aefea067153",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "36ab5fa8-96b8-459e-b9ba-cd5e1106115c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Ayat\n"
     ]
    }
   ],
   "source": [
    "name=\"Ayat\"\n",
    "print(\"My name is\", name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "714093b5-984e-4882-9aa4-03fe18efffea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name isAyat\n"
     ]
    }
   ],
   "source": [
    "name=\"Ayat\"\n",
    "print(\"My name is\"+ name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3468a11c-d9bc-4326-acff-ccbe92c46894",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My favorite number is 4\n"
     ]
    }
   ],
   "source": [
    "number= 4\n",
    "print(\"My favorite number is\", number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ff021fb0-418b-47d2-a5cd-9c46d1195b4c",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-12-10226e485b0d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mnumber\u001b[0m\u001b[1;33m=\u001b[0m \u001b[1;36m4\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"My favorite number is\"\u001b[0m\u001b[1;33m+\u001b[0m \u001b[0mnumber\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "number= 4\n",
    "print(\"My favorite number is\"+ number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "20bfd2d0-7402-4529-aa61-862c6101d139",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love eat Past and Pizza \n"
     ]
    }
   ],
   "source": [
    "food1= \"Past\"\n",
    "food2= \"Pizza\"\n",
    "print(f\"I love eat {food1} and {food2} \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4a1d0bcf-7a78-4a47-8f8d-087dbfd1f196",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love eat Past and Pizza \n"
     ]
    }
   ],
   "source": [
    "food1= \"Past\"\n",
    "food2= \"Pizza\"\n",
    "print(\"I love eat {} and {} \".format(food1,food2))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
