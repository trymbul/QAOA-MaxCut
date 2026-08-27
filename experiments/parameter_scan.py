import numpy as np
from src.qaoa import qaoa_expectation, qaoa_state
import matplotlib.pyplot as plt
from src.measurement import index_to_bitstring

gammas = np.linspace(0, np.pi, 50)
betas = np.linspace(0, np.pi, 50)

values = np.zeros((50, 50))
graph = [(0, 1), (1, 2), (0, 2)]

for i in range(len(gammas)):
    for j in range(len(betas)):
        values[i, j] = qaoa_expectation(graph, 3, gammas[i], betas[j])

i, j = np.unravel_index(np.argmax(values), values.shape)

best_value = values[i, j]
best_gamma = gammas[i]
best_beta = betas[j]

print(f"Best expectation: {best_value:.4f}")
print(f"Best gamma: {best_gamma:.4f}")
print(f"Best beta: {best_beta:.4f}")

norm = plt.Normalize(vmin=0, vmax=2)
img = plt.imshow(
    values,
    extent=[gammas[0], gammas[-1], betas[0], betas[-1]],
    origin="lower",
    aspect="auto",
    norm=norm
)
plt.scatter(best_gamma, best_beta, marker="x")
plt.xlabel("γ")
plt.ylabel("β")
plt.colorbar(img, label="Expectation value")
plt.savefig("figures/parameter_landscape.png", dpi=300, bbox_inches="tight")


plt.figure()
state = qaoa_state(graph, 3, best_gamma, best_beta)
probabilities = np.abs(state)**2
states = [index_to_bitstring(i, 3) for i in range(2**3)]
plt.bar(states, probabilities)

plt.xlabel("State")
plt.ylabel("Probability")
plt.title("QAOA measurement probabilities")
plt.savefig("figures/measurement_probabilities.png", dpi=300, bbox_inches="tight")
