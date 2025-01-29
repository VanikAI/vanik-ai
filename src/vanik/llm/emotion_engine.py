"""
Emotion Analysis Engine - Powered by Hybrid NLP Models
"""
from transformers import pipeline
import numpy as np

class EmotionAnalyzer:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )
        self.crypto_lexicon = self._load_crypto_terms()
    
    def analyze(self, text: str) -> dict:
        """Analyze text with emotion and crypto context"""
        base_emotion = self.classifier(text)[0]
        crypto_score = self._calculate_crypto_relevance(text)
        
        return {
            "emotion": self._format_emotions(base_emotion),
            "crypto_context": crypto_score,
            "recommended_response_type": self._determine_response_type(
                base_emotion,
                crypto_score
            )
        }
    
    def _calculate_crypto_relevance(self, text: str) -> float:
        # Mock implementation
        return len([w for w in text.split() if w.lower() in self.crypto_lexicon]) / len(text.split())
    
    def _format_emotions(self, emotions):
        return {e['label']: round(float(e['score']), 3) for e in emotions}
