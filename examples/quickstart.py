#!/usr/bin/env python3
# YOLOPunk 🩸 AGPL-3.0 License

"""Exemplo de uso básico do YOLOPunk.

Este script demonstra como usar as funcionalidades principais
do framework para detecção de objetos.

Requisitos:
    pip install ultralytics opencv-python

Uso:
    python examples/quickstart.py
"""

from pathlib import Path
import sys

# Adiciona o diretório raiz ao path (para importar yolopunk)
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

import yolopunk
from yolopunk import Vision
from yolopunk.utils import load_image, draw_boxes, save_image


def main():
    """🩸 Função principal do exemplo."""
    
    print("\n" + "="*60)
    print(f"🩸 YOLOPunk v{yolopunk.__version__}")
    print(f"🩸 Exemplo de Detecção de Objetos")
    print("="*60 + "\n")

    # ---------------------------------------------------------------
    # 1. Inicializar detector
    # ---------------------------------------------------------------
    print("━" * 60)
    print("🤖 Inicializando detector...")
    print("━" * 60)
    
    try:
        detector = Vision(
            model="yolov8n.pt",  # Modelo nano (mais rápido)
            device="cpu",         # Use 'cuda' se tiver GPU
            verbose=True
        )
        print(f"✅ Detector inicializado: {detector}\n")
    except ImportError as e:
        print(f"❌ Erro: {e}")
        print("\n💡 Instale as dependências:")
        print("   pip install ultralytics opencv-python")
        return

    # ---------------------------------------------------------------
    # 2. Detecção em imagem de exemplo
    # ---------------------------------------------------------------
    print("━" * 60)
    print("🔍 Detectando objetos...")
    print("━" * 60)
    
    # O YOLO vem com imagens de exemplo builtin
    # Você pode usar URLs, caminhos locais, ou 0 para webcam
    source = "https://ultralytics.com/images/bus.jpg"
    
    print(f"📍 Source: {source}")
    
    try:
        results = detector.detect(
            source=source,
            conf=0.25,    # Threshold de confiança
            iou=0.7,      # IoU para NMS
            max_det=300,  # Máximo de detecções
            save=False,   # Não salvar automaticamente
        )
        
        print(f"✅ Detecção concluída!\n")
        
        # ---------------------------------------------------------------
        # 3. Analisar resultados
        # ---------------------------------------------------------------
        print("━" * 60)
        print("📊 Resultados da detecção:")
        print("━" * 60)
        
        for i, result in enumerate(results):
            print(f"\n🖼️ Imagem {i + 1}:")
            
            # Boxes detectadas
            boxes = result.boxes
            print(f"  🎯 Objetos detectados: {len(boxes)}")
            
            # Detalhes de cada objeto
            for j, box in enumerate(boxes):
                # Coordenadas
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                
                # Confiança e classe
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = result.names[cls]
                
                print(f"\n  🔵 Objeto {j + 1}:")
                print(f"     Classe: {label}")
                print(f"     Confiança: {conf:.2%}")
                print(f"     Box: [{x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f}]")
        
        # ---------------------------------------------------------------
        # 4. Salvar resultado anotado
        # ---------------------------------------------------------------
        print("\n" + "━" * 60)
        print("💾 Salvando resultado...")
        print("━" * 60)
        
        # Diretório de resultados
        output_dir = yolopunk.RESULTS_DIR / "quickstart"
        output_dir.mkdir(exist_ok=True)
        
        # Salva imagem anotada
        output_path = output_dir / "detection_result.jpg"
        results[0].save(filename=str(output_path))
        
        print(f"✅ Resultado salvo em: {output_path}")
        
        # ---------------------------------------------------------------
        # 5. Mostrar estatísticas
        # ---------------------------------------------------------------
        print("\n" + "━" * 60)
        print("📊 Estatísticas:")
        print("━" * 60)
        
        # Conta objetos por classe
        from collections import Counter
        
        classes = [result.names[int(box.cls[0])] for box in results[0].boxes]
        class_counts = Counter(classes)
        
        print("\n📈 Objetos por classe:")
        for cls, count in class_counts.most_common():
            print(f"   {cls}: {count}")
        
        # Tempo de inferência
        if hasattr(results[0], 'speed'):
            speed = results[0].speed
            print(f"\n⏱️ Velocidade de inferência:")
            print(f"   Preprocess: {speed['preprocess']:.1f}ms")
            print(f"   Inference: {speed['inference']:.1f}ms")
            print(f"   Postprocess: {speed['postprocess']:.1f}ms")
        
    except Exception as e:
        print(f"❌ Erro durante detecção: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # ---------------------------------------------------------------
    # Final
    # ---------------------------------------------------------------
    print("\n" + "="*60)
    print("✅ Exemplo concluído com sucesso!")
    print("="*60)
    print("\n💡 Próximos passos:")
    print("   1. Teste com suas próprias imagens")
    print("   2. Experimente outros modelos (yolov8s, yolov8m, etc.)")
    print("   3. Ajuste os parâmetros de detecção (conf, iou)")
    print("   4. Explore as funções em yolopunk.utils")
    print("\n📚 Documentação: https://github.com/Crise-Ergodica/yolopunk")
    print("\n")


if __name__ == "__main__":
    main()