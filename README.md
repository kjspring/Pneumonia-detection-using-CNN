# Background
In the United States, pneumonia is the second only to the birth of a child, for the most likely reason a person is admitted to a hospital. In the U.S. over 1 million adults will be admitted for pneumonia and complications each year and 50,000 will die ([source](https://www.reuters.com/article/health-pneumonia/study-can-pneumonia-be-reliably-diagnosed-without-x-rays-idINL4N0AY04820130129)). According to UNICEF, every year on our planet 700,000 children under the age of 5 will die from complications of pneumonia. 

Symptoms of pneumonia can appear suddently. A mild case may present with limited shortness of breath and productive cough. Severe disease may include fever, respiratory distress, and sepsis. Pneumonia is caused by inflamation around the air sacs of lungs which will keep an inflicted person's lungs from getting enough oxygen into their blood. These air sacs may be filled with fluid or pus. Infections of fungi, viruses, or bacteria, or irritation from environmental factors may lead to pneumonia.

Early detection of pneumonia is critical for positive health outcomes and decreased cost of care. If caught early, pneumonia can be treated as a mild case and the patient can recover at home. Severe cases will need to be treated in the hopital and potentially the intensive care unit. The NHS founnd it cost US equivaqlent $4,718 to treat a patient with pneumonia ([source](https://www.tandfonline.com/doi/full/10.1080/13696998.2022.2090734)). According to guidelines by the American Thoracic Society and Infectious Disease Society of America, x-ray identification of the presence of infiltrates (white spots) in the lungs of a patient with history of symptoms is the gold standard for diagnosis of pneumonia.

It may take the radiologist a few minutes to identify pneumonia from with their domain knowledge but the reading could be delayed due to the number of other radiological images a radiologist needs to read and diagnose. The Association of American Medical Colleges (AAMC) projects to have a serious shortage of radiologists by 2033. This is in contrast of the increase in medical imaging of about 5% a year. A shortage of radiologists will lead to worse patient outcomes as the turnaround time for them to make a diagnosis on a medical image increases.

## Business Problem

Our company, United Healthcare, is an medical insurance company that provides health insurance through private and Affordable Care Act (ACA) health insurance exchanges. We are expanding our coverage to more rural clients and hospitals but this is where the shortage of specialty care such as radiology is in crisis. Reducing this bottleneck in pneumonia diagnosis will reduce the time a patient is admitted to the hospital and reduce costs associated with this care.

With the increase cost and lower supply of radiologists, United Healthcare needs to **develop an application to classify chest x-ray images with pneumonia or without (normal)**. Those predicted to have pneumonia would be forwarded to a radiologist for a confirmed diagnosis. This will lessen the burden and cost of radiologists reviewing chest x-rays that are not indicative of pneumonia.

## Stakeholders
- United Healthcare executives
- Healthcare workers

## Methods
Convolutional Neural Networks (CNN) is a machine learning technique that reduces the high dimensionality of images without losing its information. CNNs have outperformed other machine learning algorithms in image classification.

![Convolutional Neural Network](https://miro.medium.com/max/828/1*vkQ0hXDaQv57sALXAJquxA.webp)

While densly connected neural networks learn global patterns in ther input feature space, convolution layers learn local paterns, that are found in 2-dimensional windows. This allows CNNs to learn patterns that are translation-invariant, something learned in one part of the image can be reused in another part. CNNs can also learn spatial heirarchies of patterns. The first layer of a CNN learns small local patterns such as edges. The next layer will learn larger patterns.

![CNN spatial hierarchies](img/spatial_hierarchy.PNG)

## Model Results

Include plot showing Accuracy, Recall, and Specificity between the 6 models

## Pneumonia Classification App

## Conclusions

## References
