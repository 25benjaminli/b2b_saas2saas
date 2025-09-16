from b2b_saas2saas import get_random_saas_idea
import dotenv
dotenv.load_dotenv()

idea = get_random_saas_idea()
print(idea)