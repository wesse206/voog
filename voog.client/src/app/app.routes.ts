import { Routes } from '@angular/router';
import { AfwesigOnderwyserComponent } from './afwesig-onderwyser/afwesig-onderwyser.component';
import { HomeComponent } from './home/home.component';
import { VoogComponent } from './voog/voog.component';

export const routes: Routes = [
    { path: '', component: HomeComponent},
    { path: 'onderwyser-afwesig', component: AfwesigOnderwyserComponent },
    { path: 'voog', component: VoogComponent}
];
