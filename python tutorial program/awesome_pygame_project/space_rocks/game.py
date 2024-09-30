{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b8fa9027-d557-4a72-b82b-318747a548df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 2.6.0 (SDL 2.28.4, Python 3.12.4)\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    }
   ],
   "source": [
    "import pygame\n",
    "\n",
    "class SpaceRocks:\n",
    "    def __init__(self):\n",
    "        self._init_pygame()\n",
    "        self.screen = pygame.display.set_mode((800,600))\n",
    "\n",
    "    def main_loop(self):\n",
    "        while True:\n",
    "            self._handle_input()\n",
    "            self._process_game_logic()\n",
    "            self._draw()\n",
    "\n",
    "    def _init_pygame(self):\n",
    "        pygame.init()\n",
    "        pygame.display.set_caption(\"Space Rocks\")\n",
    "\n",
    "    def _handle_input(self):\n",
    "        pass\n",
    "\n",
    "    def _process_game_logic(self):\n",
    "        pass\n",
    "\n",
    "    def _draw(self):\n",
    "        self.screen.fill((0,0,255))\n",
    "        pygame.display.flip()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7fe942a-63a9-4775-bef9-c1878ef8046a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
