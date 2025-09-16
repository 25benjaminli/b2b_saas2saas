# B2B SaaS to SaaS

This is an AI-powered SaaS generator that can be used to make you (or lose you) millions!

https://pypi.org/project/b2b-saas2saas/

## Installation

```bash
pip install b2b_saas2saas
```

Add your OpenAI key to a .env file. 
```
OPENAI_API_KEY=your_key
```

## Usage

```python
from b2b_saas2saas import get_random_saas_idea
import dotenv
dotenv.load_dotenv()

idea = get_random_saas_idea()
print(idea)
```

dependencies:
- openai
- python-dotenv

Use at your own risk - I'm not liable for any damages!

License: MIT