from rouge_score import rouge_scorer

def eval_rouge(original, summerized):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(original, summerized)
    print(scores)

