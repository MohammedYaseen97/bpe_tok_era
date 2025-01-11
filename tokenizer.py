import regex as re

def get_stats(ids, freq):
    for pair in zip(ids[:-1], ids[1:]):
        freq[pair] = freq.get(pair, 0) + 1

def merge(ids, pair, idx):
    newids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

def _build_vocab(merges):
    vocab = {idx: bytes([idx]) for idx in range(256)}
    for (p0, p1), idx in merges.items():
        vocab[idx] = vocab[p0] + vocab[p1]
    return vocab

class CustomTokenizer:
    def __init__(self, model_file):
        self.merges, self.special_tokens, self.vocab = self.load(model_file)
        self.pattern = r"""(?i) 's|'t|'re|'ve|'m|'ll|'d| ?\b[\p{L}\u0900-\u0963|\u0966-\u097F]+\b| ?\b[\p{L}\u0C80-\u0C9E|\u0CA0-\u0CFF]+\b| ?[\p{N}]+| ?[.,!?;:'"-]| ?[\u0964-\u0965]| ?[\u0C9E-\u0C9F]| ?[^\s\p{L}\p{N}\u0900-\u097F\u0C80-\u0CFF]+| \s+(?!\S)| \s+"""
        self.regex = re.compile(self.pattern)

    def load(self, model_file):
        merges = {}
        special_tokens = {}
        idx = 256
        with open(model_file, 'r', encoding="utf-8") as f:
            version = f.readline().strip()
            assert version == "minbpe v1"
            pattern = f.readline().strip()
            num_special = int(f.readline().strip())
            for _ in range(num_special):
                special, special_idx = f.readline().strip().split()
                special_tokens[special] = int(special_idx)
            for line in f:
                idx1, idx2 = map(int, line.split())
                merges[(idx1, idx2)] = idx
                idx += 1
        vocab = _build_vocab(merges)
        return merges, special_tokens, vocab

    def _encode_chunk(self, chunk_bytes: bytes) -> list[int]:
        tokens = list(chunk_bytes)
        while len(tokens) >= 2:
            stats = {}
            get_stats(tokens, stats)
            pair = min(stats, key=lambda p: self.merges.get(p, float("inf")))
            if pair not in self.merges:
                break
            idx = self.merges[pair]
            tokens = merge(tokens, pair, idx)
        return tokens

    def encode(self, text: str, allowed_special="none") -> list[int]:
        special = {}
        if allowed_special == "all":
            special = self.special_tokens
        elif allowed_special == "none":
            special = {}
        elif isinstance(allowed_special, set):
            special = {k: v for k, v in self.special_tokens.items() if k in allowed_special}
        
        if not special:
            chunk_texts = re.findall(self.regex, text)
            ids_list = []
            for text in chunk_texts:
                chunk_bytes = text.encode("utf-8")
                ids = self._encode_chunk(chunk_bytes)
                ids_list.extend(ids)
            return ids_list

        special_pattern = "(" + "|".join(re.escape(token) for token in special) + ")"
        parts = re.split(special_pattern, text)
        ids = []
        for part in parts:
            if part in special:
                ids.append(special[part])
            else:
                chunk_texts = re.findall(self.regex, part)
                for text in chunk_texts:
                    chunk_bytes = text.encode("utf-8")
                    ids.extend(self._encode_chunk(chunk_bytes))
        return ids 