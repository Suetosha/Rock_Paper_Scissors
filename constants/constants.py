from lexicon.lexicon import LEXICON_RU

list_of_variants = [LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper']]

rules = {LEXICON_RU['rock']: LEXICON_RU['scissors'],
         LEXICON_RU['scissors']: LEXICON_RU['paper'],
         LEXICON_RU['paper']: LEXICON_RU['rock']
         }

emoji = {LEXICON_RU['rock']: '🗿',
         LEXICON_RU['scissors']: '✂',
         LEXICON_RU['paper']: '📜'
         }
