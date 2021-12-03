from rouge_score import rouge_scorer

def eval_rouge(original, summerized_bart, summerized_pegasus):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    print("BART:\n")
    scores = scorer.score(original, summerized_bart)
    print(scores)
    print("PEGASUS:\n")
    scores = scorer.score(original, summerized_pegasus)
    print(scores)


