import random
from collections import defaultdict
import os
import logging

class FantasyStoryGenerator:
    def __init__(self):
        self.markov_chains = defaultdict(list)
        self.story_elements = {
            'heroes': ['el joven mago', 'la valiente guerrera', 'el sabio druida'],
            'villains': ['el dragón oscuro', 'el hechicero maligno', 'la reina de las sombras'],
            'locations': ['el bosque encantado', 'la montaña maldita', 'el castillo antiguo'],
            'objects': ['la espada mágica', 'el cristal del poder', 'el grimorio ancestral'],
            'conflicts': ['buscar el objeto perdido', 'derrotar al villano', 'romper la maldición']
        }
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def load_training_texts(self, directory_path):
        """
        Carga todos los archivos .txt de un directorio como textos de entrenamiento
        """
        training_texts = []
        try:
            if not os.path.exists(directory_path):
                raise FileNotFoundError(f"El directorio {directory_path} no existe")

            txt_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

            if not txt_files:
                self.logger.warning(f"No se encontraron archivos .txt en {directory_path}")
                return training_texts

            for filename in txt_files:
                file_path = os.path.join(directory_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        text = file.read()
                        if text:
                            training_texts.append(text)
                            self.logger.info(f"Archivo cargado exitosamente: {filename}")
                        else:
                            self.logger.warning(f"Archivo vacío: {filename}")
                except Exception as e:
                    self.logger.error(f"Error al leer el archivo {filename}: {str(e)}")

        except Exception as e:
            self.logger.error(f"Error al procesar el directorio: {str(e)}")

        return training_texts

    def train_markov(self, texts):
        """Entrena las cadenas de Markov con textos de ejemplo"""
        if not texts:
            self.logger.warning("No hay textos de entrenamiento disponibles")
            return

        for text in texts:
            words = text.split()
            for i in range(len(words) - 3):
                key = (words[i], words[i + 1], words[i + 2])
                self.markov_chains[key].append(words[i + 3])

        self.logger.info(f"Entrenamiento completado con {len(texts)} textos")

    def generate_paragraph(self, start_words, length=50):
        """Genera un párrafo usando cadenas de Markov"""
        if len(start_words) < 3:
            return ""

        current = tuple(start_words[:3])
        result = list(current)

        for _ in range(length):
            if current not in self.markov_chains:
                break
            next_word = random.choice(self.markov_chains[current])
            result.append(next_word)
            current = (current[1], current[2], next_word)

        return ' '.join(result)

    def generate_story(self):
        """Genera una historia completa usando plantillas y cadenas de Markov"""
        hero = random.choice(self.story_elements['heroes'])
        villain = random.choice(self.story_elements['villains'])
        location = random.choice(self.story_elements['locations'])
        magic_object = random.choice(self.story_elements['objects'])
        conflict = random.choice(self.story_elements['conflicts'])

        story_structure = {
            'introduction': [
                f"En un reino lejano, {hero} vivía tranquilamente hasta que {villain} apareció en {location}.",
                f"En las tierras de {location}, {hero} escuchó rumores sobre {villain}.",
                f"{hero} habitaba en {location}, pero la llegada de {villain} cambió todo."
            ],
            'conflict': [
                f"Para enfrentarlo, decidió {conflict} usando {magic_object}.",
                f"Su única esperanza era encontrar {magic_object} y {conflict}.",
                f"{magic_object} se convertiría en la clave para {conflict}."
            ],
            'development': [
                "En medio del caos, un nuevo desafío surgió.",
                "Mientras tanto, secretos olvidados comenzaron a revelarse.",
                "El viaje se volvió más peligroso de lo que imaginaban."
            ],
            'climax': [
                f"En una épica batalla final, {hero} se enfrentó a {villain}.",
                "La confrontación decisiva marcó un punto de no retorno.",
                f"{villain} desplegó todo su poder, pero {hero} no se rindió."
            ],
            'resolution': [
                f"Finalmente, la paz retornó al reino, y {hero} fue recordado como un héroe legendario.",
                "Con el villano derrotado, el reino volvió a florecer.",
                f"{hero} regresó a {location}, sabiendo que su valentía había salvado a todos."
            ]
        }

        full_story = []
        for section, options in story_structure.items():
            selected_template = random.choice(options)
            if section == 'development':
                expanded_paragraph = self.generate_paragraph(selected_template.split()[:3], 50)
                full_story.append(expanded_paragraph if expanded_paragraph else selected_template)
            else:
                full_story.append(selected_template)

        return '\n\n'.join(full_story)

def main():
    # Crear una instancia del generador
    generator = FantasyStoryGenerator()

    # Directorio donde están los cuentos
    stories_dir = "C:/Users/agonz/OneDrive - Instituto Politecnico Nacional/ESCOM/Sem6/Compiladores/proyect/Avance5/cuentos"  # Cambia esto a la ruta de tu directorio

    # Cargar y entrenar con los textos
    training_texts = generator.load_training_texts(stories_dir)
    generator.train_markov(training_texts)

    # Generar una historia
    story = generator.generate_story()

    # Imprimir la historia
    print("\n=== HISTORIA GENERADA ===")
    print(story)
    print("=======================\n")

if __name__ == "__main__":
    main()
