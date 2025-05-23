# Enigma Machine Simulator 🔐

This project simulates the working of a World War II-era **Enigma Machine**, focusing on its encryption and decryption mechanics. The implementation includes rotors, a plugboard, a reflector, and a ring setting system. The goal is to replicate the core behavior of the Enigma machine — namely, its symmetric encryption system where the same process is used for both encoding and decoding messages.

## Features

- **Rotor System Simulation**: Each rotor has its own internal wiring and notch settings. Rotors advance with each key press, changing the cipher dynamically.
- **Reflector Logic**: Implements a basic reflector that ensures encryption is symmetric.
- **Plugboard Support**: Configurable plugboard wiring enables letter substitutions both before and after the rotor transformations.
- **Real-Time Step Logging**: Each character's transformation is logged step-by-step for educational and debugging purposes.
- **Reset Functionality**: Allows resetting rotor positions to ensure proper decryption of previously encrypted text.
- **Modular Design**: Classes such as `ROTOR`, `RING`, and `ENIGMA_MACHINE` provide a modular and extensible architecture for customization.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kinglord1090/enigma-machine-simulator.git
   ```

## Usage

1. Navigate to the project directory:
   ```bash
   cd enigma-machine-simulator
   ```
2. Run the simulation:
    ```bash
    python enigma-sim.py
    ```
3. The program will:
   - Initialize rotors with custom or default wiring.
   - Configure plugboard and ring settings.
   - Encrypt a hardcoded plaintext.
   - Reset the machine and decrypt the ciphertext back to the original message.
4. Observe the step-by-step transformation in the console output.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

  - Alan Turing, whose brilliant work in breaking the original Enigma code changed the course of history and laid the foundations of modern computing.
  - Inspired by the historical design of the Enigma Machine created by Arthur Scherbius.
  - Thanks to Python’s built-in string and random modules for character management and rotor wiring generation.
  - Educational materials and simulations on cryptography that provided insight into rotor-based cipher systems.
