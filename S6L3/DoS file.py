import socket
import random
import time

def udp_connection_test():
    # 1. Input dell'IP Target
    target_ip = input("Inserisci l'IP del server di test: ")
    
    # 2. Input della Porta Target
    try:
        target_port = int(input("Inserisci la porta UDP (es. 5005): "))
        
        # 3. Numero di pacchetti da inviare
        num_packets = int(input("Quanti pacchetti di test vuoi inviare? "))
    except ValueError:
        print("Errore: Inserisci numeri validi per porta e quantità.")
        return

    # Creazione del socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"\nInizio test verso {target_ip}:{target_port}...")

    sent_count = 0
    try:
        for i in range(num_packets):
            # 4. Costruzione del pacchetto da 1 KB (1024 byte)
            # Generiamo byte casuali come richiesto
            payload = random.randbytes(1024)
            
            # Invio del pacchetto
            sock.sendto(payload, (target_ip, target_port))
            
            sent_count += 1
            print(f"Pacchetto {sent_count}/{num_packets} inviato con successo.")
            
            # Introduciamo un piccolo ritardo per rendere il test controllato
            # e non saturare la banda (approccio Blue Team/Monitoraggio)
            time.sleep(0.1) 

    except Exception as e:
        print(f"Errore durante l'invio: {e}")
    finally:
        sock.close()
        print(f"\nTest concluso. Pacchetti totali inviati: {sent_count}")

if __name__ == "__main__":
    udp_connection_test()