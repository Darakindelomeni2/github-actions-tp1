# Réponses aux questions

## 3. Quelle est l'utilité de ce répertoire ? 
Le répertoire .github/workflows a pour but de contenir le fichier yaml contenant l'automatisation de notre pipeline avec toute la description des github actions

## 8. Accède à l'onglet "Actions" de ton repository sur GitHub. Que constates-tu ? 
Dans l'onglet ça m'affiche un workflow qui a été lancé avec le nom du message de commit
Il indique que c'est hello.yaml qu'il a été exécuté On Push et contient 3 étapes
**Set up job**
Current runner version: '2.325.0'
Runner Image Provisioner
Operating System
Runner Image
GITHUB_TOKEN Permissions
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Complete job name: hello
0s
**Hello step**
Run echo "Hello World from GitHub Actions!"
Hello World from GitHub Actions!
1s
**complete step**
Cleaning up orphan processes

## 10. Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions. Que constates-tu ?
test.yaml s'est exécuté deux fois avec sous titre l'un qui run test.yaml et l'autre hello.yaml
Le job test installe python et ses dépendances, fais les tests et désinstalle pyton

## 11. Que se passe-t-il lors du prochain push ?
Le run test bug mais j'avais déjà été prévenu par mon correcteur de syntaxe vscode

## 14.  Que constates-tu après le push ? 
Le test.yaml a exécuté 3 jobs, un pour chaque version de python de la matrice

## 18. Que se passe-t-il avec ton workflow de commentaires ?
La pull request est bien sur github et est passée sans soucis puisque pas de conflit

## 21.  Que constates-tu après avoir poussé ces modifications ?
J'ai un build status badge passed dans le readme

## 24. Commit et pousse ces modifications. Que constates-tu dans l'onglet Actions ?
Il a build l'image docker

## 27. Commit et pousse ces modifications. Vérifie l'onglet Actions et télécharge l'artifact généré. Que contient-il ?
Le metrics.json
{
  "accuracy": 0.929,
  "precision": 0.934,
  "recall": 0.845,
  "f1_score": 0.889
}

## 30.  Pousse plusieurs fois les modifications et observe les résultats. Que constates-tu ?
Aléatoirement ça échoue

## 33. Va dans l'onglet Actions sur GitHub et déclenche manuellement ce workflow. Que constates-tu ?
Il m'indique juste qu'il a un workflow_dispatch event trigger mais fonctionne

## 36.  Vérifie dans l'onglet "Releases" de ton repository. Que constates-tu ?
J'ai un tag v1.0.0 qui est apparu

## 38. Ajoute plus de commentaires à ton fichier model.py et pousse-le. Vérifie l'artifact de documentation. Que contient-il ?
A près correction du fichier qui n'est pas bon j'obtiens l'artefact avec le contenu suivant
```bash
<a id="model"></a>

# model

<a id="test_model"></a>

# test\_model

<a id="metrics"></a>

# metrics
```

## 40. Ajoute une nouvelle dépendance à requirements.txt et pousse-la. Exécute ce workflow deux fois. Que constates-tu au niveau du temps d'exécution ?

## 42. Pousse ce workflow et observe la visualisation dans l'onglet Actions. Que constates-tu sur l'ordre d'exécution des job ?

## 44. Pousse ce workflow et explore la visualisation complète du pipeline MLOps. Que penses-tu de cette structure pour un projet ML réel ?